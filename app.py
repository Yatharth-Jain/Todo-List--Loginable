from website import create_app

app=create_app()
print("Hello")
if __name__=='__main__':
    app.run(debug=True)