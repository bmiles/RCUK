RCUK
====

RCUK Gateway to Research 2013 Hack for SME's.

## How to set up the AngularJS frontend
1. Change to the `app` directory
2. Install node dependencies with `npm install` (requires [node.js] and [npm])
3. Install [bower] and [grunt]: `npm install -g bower grunt`
4. Install bower dependencies with `bower install`
5. Build the frontend app with `grunt build`

## How to set up Python backend environment
1. Set up and activate virtual environment e.g. using [virtualenvwrapper]
2. Install dependencies: `pip install -r requirements.txt`
4. Install foreman `gem install foreman` (requires ruby)
5. Create a `.env` file in the root folder:

        MONGOLAB_URI=<connection string>
        EVE_DEBUG=1
6. Launch the server with `foreman start`

[node.js]: http://nodejs.org
[npm]: https://npmjs.org
[bower]: http://bower.io
[grunt]: http://gruntjs.com
[virtualenvwrapper]: https://pypi.python.org/pypi/virtualenvwrapper
