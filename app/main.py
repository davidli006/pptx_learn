from flask import Flask, render_template

app = Flask(__name__)

# 配置
app.template_folder = 'templates'
app.static_folder = 'static'
app.static_url_path = '/static'

# 路由
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
