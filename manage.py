import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser("Runner")
    parser.add_argument('action', type=str, nargs=None, help="webpage")
    args = parser.parse_args()


    args.action == 'webpage'
    from search_engine import app
    app.run(debug=True, port=9000)
