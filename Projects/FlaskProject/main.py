from website import create_app

# pulls in the function from the website folder to initiate the app
app = create_app()


# only if import this file, it will run
if __name__ == '__main__':
    # will run our application into a web server
    # turn off debug when in production.
    app.run(debug=True)
