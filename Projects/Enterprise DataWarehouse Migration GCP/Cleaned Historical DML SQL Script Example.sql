MERGE INTO `edw_product_storage` as tgt 
USING
(
    WITH 
    Shipcase AS
    (
      SELECT
        SKU_ID,
        CFC_ID, 
        AUTH_SUPPLIER_NO, 
        ROTATION_FLAG,
        CASE_SIZE,
        START_DATE,
         END_DATE,
      DIMENSION_UOM,
      SHIPCASE_ID,
      WIDTH, 
      HEIGHT,
      DEPTH,
      finance_shipcase_category,
      SELLING_GROUP_SKU
      FROM
        `table_one`
      WHERE
        1 = 1
      QUALIFY
        ROW_NUMBER() OVER ( PARTITION BY SKU_ID, timestamp_micros(start_date) ORDER BY CFC_ID asc , timestamp_micros(END_DATE) desc) = 1 
     --   AND  SKU_ID IS NOT NULL and sku_id = '25370011'
    ),  
    irp AS 
    (
      SELECT
        bitm_numb,
        cast(orgu_numb as integer) as orgu_numb,
        LOCATION,
        DIFFERENTIATION,
        PUTAWAY_GROUP,
        CPP,
        EACH_PER_TRAY,
        EACH_PER_TOTE,
        BOX_EACH
      FROM
        `table_two` 
      where 1 = 1 
      qualify
        ROW_NUMBER() OVER ( PARTITION BY bitm_numb ORDER BY cast(orgu_numb as integer)  ) = 1
    ),
    mvw AS 
    (
      SELECT
        bitm_numb,
        cast(orgu_numb as integer) as orgu_numb,
        storage_Segregation,
        volume
      FROM
        `table_three` 
      WHERE
        1 = 1
        --AND bitm_numb = '10054011'
      QUALIFY
        ROW_NUMBER() OVER (PARTITION BY bitm_numb ORDER BY cast(orgu_numb as integer)) = 1
    )
    ,Volume AS
    (
      select ds.shipcase_id sku, 
      case when   mvw.uom_code in ('OZ','CL', 'L','ML')  
                   then round( ifnull(cast(msc.weight as float64),ifnull(cast(mvw.size_pack_mltp as float64),1)*(case when mvw.uom_code='Mg' 
                                                                           then 0.000001
                                                                           when mvw.uom_code in ('GR','ML') 
                                                                           then 0.001
                                                                           when mvw.uom_code in ('CL','CM') 
                                                                           then 0.01
                                                                           when mvw.uom_code='IN'  
                                                                           then 0.0254
                                                                           when mvw.uom_code='OZ'  
                                                                           then 0.0284
                                                                           when mvw.uom_code='LB' 
                                                                           then 0.4536
                                                                           when mvw.uom_code='DOZ'  
                                                                           then 12
                                                                           else 1 
                                                                       end)*cast(mvw.size_amnt as float64)),9)
                   else round((case when ds.dimension_uom='FT' 
                                then 28.317
                                when  ds.dimension_uom='IN' 
                                then 0.0164
                                when  ds.dimension_uom='M' 
                                then 1000
                                when  ds.dimension_uom='CM' 
                                then 0.001
                                else 0.001 
                           end)*ds.height*ds.width*ds.depth,9) 
              end volume_l,
      start_date
              
      FROM 
    (
        select * from shipcase) ds
        left join 
        (  
        select 
        stit_numb, 
        sze.* 
        from `table_four` as st
        left join
        `table_five` as sze
        on 
        SZE.SIZE_NUMB=ST.SIZE_NUMB
        ) mvw
        on 
          cast(mvw.stit_numb as float64)=floor(ds.shipcase_id/1000)*1000
            
        left join 
        (
          select * 
          from  
          (
            select 
              count(*) over (partition by selling_group_sku) variant, 
              selling_group_sku ,
              weight, 
              dense_rank() over (partition by selling_group_sku order by shipcase_id) rnk 
            from 
            (
              select * from `table_one`
            ) dim_shipcase_temp
            where TIMESTAMP_MICROS(end_date)>current_timestamp()
              and price_uom='KG'  
              and range_status='RANGED'
              and cast(dim_shipcase_temp.shipcase_id as string) in (select sku from `table_six`) 
              and msc_flag=true
           )      
       where weight is not null 
      and variant<=2 
      and rnk=1
        ) msc  
      on msc.selling_group_sku=ds.selling_group_sku
      WHERE TIMESTAMP_MICROS(ds.end_date) > current_timestamp()
      AND  (ds.finance_shipcase_category > 9 OR ds.finance_shipcase_category IS NULL)   
      AND 1 = 1
    QUALIFY ROW_NUMBER() OVER ( PARTITION BY SKU_ID, start_date ORDER BY CFC_ID desc) = 1                              
  ),
  TEMP_SRC AS
    (
    SELECT
      Generate_UUID() AS Product_Storage_UUID,
      t1.SKU_ID AS SKU_ID,
    t1.CFC_ID, 
    t1.END_DATE, 
    t1.AUTH_SUPPLIER_NO, 
    t2.ORGU_NUMB,
      t1.ROTATION_FLAG AS ROTATION_FLAG,
      t2.STORAGE_SEGREGATION AS STORAGE_SEGREGATION,
      COALESCE (t3.location,t3.DIFFERENTIATION, t3.PUTAWAY_GROUP) AS LOCATION,
      COALESCE (t3.DIFFERENTIATION, t3.PUTAWAY_GROUP, t3.location) AS PICKFACE,
      case when t3.location like 'F1D4%A' or t3.location like 'F2D4%A'
                or t3.location like 'Z1C5%' or t3.location like 'Z1D5%'
                or t3.location like 'Z3B5%' or t3.location like 'Z3C5%'
                or t3.location like 'Z3D5%' or t3.location like 'Z3Z5%'
                or t3.location like 'Z3A5%' or t3.location like 'Z1B5%'
                or t3.location like 'C2B5%' or t3.location like 'C2C5%'
                or t3.location like 'C2D5%' or t3.location like 'C3A%'
                or t3.location like 'C3B5%' or t3.location like 'C3C5%'
                or t3.location like 'C3D5%' or t3.location like 'P1C%'
                or t3.location like 'P1D%'
            then 'Pallet'
           when t3.location like 'Z1B1%' or t3.location like 'Z1B2%'
                or t3.location like 'Z1C1%' or t3.location like 'Z1C2%'
                or t3.location like 'Z1D1%' or t3.location like 'Z1D2%'
                or t3.location like 'AZPB1' or t3.location like 'AZPC1'
                or t3.location like 'AZPD1' or t3.location like 'Z2B%'
                or t3.location like 'Z2C%' or t3.location like 'Z2D%'
                or t3.location like 'Z3B%' or t3.location like 'Z3C%'
                or t3.location like 'Z3D%'
            then 'Tray'
           when t3.location like 'Z3A1%' or t3.location like 'Z3A2%' or
                t3.location like 'Z3A3%' or t3.location like 'Z3A4%' or
                t3.location like 'Z3Z1%' or t3.location like 'Z3Z2%' or
                t3.location like 'Z3Z3%' or t3.location like 'Z3Z4%'
            then 'Box'
           when COALESCE (t3.DIFFERENTIATION,t3.PUTAWAY_GROUP,t3.location) like '%Tote%' then 'Tote'
           when COALESCE (t3.DIFFERENTIATION,t3.PUTAWAY_GROUP,t3.location) like '%Tray%' then 'Tray'
           when COALESCE (t3.DIFFERENTIATION,t3.PUTAWAY_GROUP,t3.location) like '%Pallet%' then 'Pallet'
           when COALESCE (t3.DIFFERENTIATION,t3.PUTAWAY_GROUP,t3.location) like '%Manual%' then 'MSC'
           when COALESCE (t3.DIFFERENTIATION,t3.PUTAWAY_GROUP,t3.location) like '%OSR%' then 'Tote'
           when COALESCE (t3.DIFFERENTIATION,t3.PUTAWAY_GROUP,t3.location) like '%Void%' then 'Tote'
      end as PICKFACE_CONTAINER,
      greatest(case when CAST(t3.cpp AS INTEGER)>1 then COALESCE(floor(cast(t3.cpp as integer)*t1.case_size), floor(2000000/coalesce(cast(t2.volume as float64),1000*t4.volume_l)))
                else floor(2000000/COALESCE(cast(t2.volume as float64),1000*t4.volume_l))
               end,
                COALESCE(cast(t3.each_per_tray as integer),floor(100000/COALESCE(cast(t2.volume as float64),1000*t4.volume_l))),
                COALESCE(cast(t3.each_per_tote as integer),floor(40000/COALESCE(cast(t2.volume as float64),1000*t4.volume_l))),
                COALESCE(cast(t3.box_each as integer),floor(5000/COALESCE(cast(t2.volume as float64),1000*t4.volume_l)))
               ) as quantity_per_pallet,
      greatest (COALESCE(cast(t3.each_per_tray as integer),floor(100000/COALESCE(cast(t2.volume as float64),1000*t4.volume_l))),
                COALESCE(cast(t3.each_per_tote as integer),floor(40000/COALESCE(cast(t2.volume as float64),1000*t4.volume_l))),
                COALESCE(cast(t3.box_each as integer),floor(5000/COALESCE(cast(t2.volume as float64),1000*t4.volume_l)))
                ) as quantity_per_tray,
      greatest (COALESCE(cast(t3.each_per_tote as integer),floor(40000/COALESCE(cast(t2.volume as float64),1000*t4.volume_l))),
                COALESCE(cast(t3.box_each as integer),floor(5000/COALESCE(cast(t2.volume as float64),1000*t4.volume_l)))
                ) as quantity_per_tote,
      COALESCE(cast(t3.box_each as integer),floor(5000/COALESCE(cast(t2.volume as float64),1000*t4.volume_l))) as quantity_per_box,
      t5.PREFER_STORAGE_SCHEME_A AS STORAGE_SCHEME,
      case when t2.STORAGE_SEGREGATION like 'MBF%' then 'Frozen'
            when t2.STORAGE_SEGREGATION like 'MBC%' then 'Chilled'
            when t2.STORAGE_SEGREGATION like 'CBC%' or t2.STORAGE_SEGREGATION like 'MBA%' then 'Ambient'
      end as STORAGE_TEMPERATURE,
    CASE 
     WHEN date(TIMESTAMP_MICROS(End_Date)) = '2037-12-31' THEN TIMESTAMP('2999-12-31 23:59:59+00') 
    ELSE TIMESTAMP_MICROS(End_Date) 
    END AS EndTime, --to be used in non_key_hash and also source of record_end_datetime
      timestamp_micros(t1.START_DATE) as Start_Date
    FROM
      Shipcase AS t1
    LEFT JOIN
      mvw AS t2
    ON
      t1.SKU_ID = t2.BITM_NUMB
    LEFT JOIN
      irp AS t3
    ON
      t1.SKU_ID = t3.BITM_NUMB
      and t2.ORGU_NUMB = t3.ORGU_NUMB
    LEFT JOIN
    Volume AS t4
    ON
      t1.SKU_ID = CAST(T4.SKU AS STRING)
      and t1.start_Date = t4.start_DAte
    LEFT JOIN
      `table_seven` as t5 
    ON
      t1.SKU_ID = t5.SKU_ID
    )
  SELECT
    * except (START_DATE, END_DATE, CFC_ID, AUTH_SUPPLIER_NO), -- these fields are not in target table schema
      -- AUDIT FIELDS
    MD5(CONCAT(IFNULL(SKU_ID, '')
      )) AS Key_Hash_Column,
    MD5(CONCAT(
      IFNULL(ROTATION_FLAG, ''),
      IFNULL(STORAGE_SEGREGATION, ''),
      IFNULL(LOCATION, ''),
      IFNULL(PICKFACE, ''),
      IFNULL(PICKFACE_CONTAINER, ''),
      IFNULL(CAST(QUANTITY_PER_PALLET AS STRING), ''),
      IFNULL(CAST(QUANTITY_PER_TRAY AS STRING), ''),
      IFNULL(CAST(QUANTITY_PER_TOTE AS STRING), ''),
      IFNULL(CAST(QUANTITY_PER_BOX AS STRING), ''),
      IFNULL(STORAGE_SCHEME, ''),
      IFNULL(STORAGE_TEMPERATURE, ''),
      IFNULL(CAST(start_Date as string), ''), -- this is the logic for record_end_datetime on line 362 to 370
      IFNULL(CAST(Endtime as string), '')
      )) AS Non_Key_Hash_Column,
      start_Date AS Record_Start_DateTime,
    FALSE AS Is_Deleted,
    'dataplatform-edw' AS Inserted_By,
    CURRENT_TIMESTAMP() as Insert_DateTime,
    CAST(NULL AS string) Modified_By,
    CAST(NULL AS timestamp) Modified_DateTime,
    "Ocean BQ" AS Source_Name
    FROM
      TEMP_SRC
  
    WHERE
   MD5(CONCAT(IFNULL(SKU_ID, '')
    )) is not null
 ) AS SRC
ON
  src.Key_Hash_Column = tgt.Key_Hash_Column AND
  src.Non_Key_Hash_Column = tgt.Non_Key_Hash_Column
WHEN NOT MATCHED BY TARGET
THEN
	INSERT
		( 
		   Product_Storage_UUID,
		   SKU_ID,
		   ROTATION_FLAG,
		   STORAGE_SEGREGATION,
		   LOCATION,
		   PICKFACE,
		   PICKFACE_CONTAINER,
		   QUANTITY_PER_PALLET,
		   QUANTITY_PER_TRAY,
		   QUANTITY_PER_TOTE,
		   QUANTITY_PER_BOX,
		   STORAGE_SCHEME,
		   STORAGE_TEMPERATURE,
		   -- AUDIT FIELDS
		   Key_Hash_Column,
		   Non_Key_Hash_Column,
		   Record_Start_DateTime,
		   Record_End_DateTime,
		   Is_Deleted,
		   Inserted_By,
		   Insert_DateTime,
		   Modified_By,
		   Modified_DateTime,
		   Source_Name
		)
	VALUES
		( 
		   Product_Storage_UUID,
		   SKU_ID,
		   ROTATION_FLAG,
		   STORAGE_SEGREGATION,
		   LOCATION,
		   PICKFACE,
		   PICKFACE_CONTAINER,
		   QUANTITY_PER_PALLET,
		   QUANTITY_PER_TRAY,
		   QUANTITY_PER_TOTE,
		   QUANTITY_PER_BOX,
		   STORAGE_SCHEME,
		   STORAGE_TEMPERATURE,
		   -- AUDIT FIELDS
		   Key_Hash_Column,
		   Non_Key_Hash_Column,
		   Record_Start_DateTime,
		   Record_End_DateTime,
		   Is_Deleted,
		   Inserted_By,
		   Insert_DateTime,
		   Modified_By,
		   Modified_DateTime,
		   Source_Name
		)

;
