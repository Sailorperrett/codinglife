from flask import Flask
import ghhops_server as hs

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/tree",
    name="tree",
    description="test",
    icon="",
    inputs=[
        hs.HopsNumber("input", "i", "test")
    ],
    outputs=[
        hs.HopsNumber("output", "o", "test")
    ]
)
def tree(input):
    return input


def main():
    app.run()


if __name__ == "__main__":
    app.run()
