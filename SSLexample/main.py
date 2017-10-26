#!/usr/bin/env python3

from flask import Flask, request, url_for, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template(
                'index.html',
                user_address=request.remote_addr,
                browser=request.user_agent.browser
            )

if __name__ == '__main__':
    app.run(ssl_context=('cert/server.crt', 'cert/server.key'))
