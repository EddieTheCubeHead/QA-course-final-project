# PokeAPI API and performance tests

## Running the tests

### Creating venv and installing requirements

If you are not using a tool like PyCharm that creates a venv for you automatically
you need to manually create or move to the virtual environment

Creating the virtual environment is done with python's venv module:
`python -m venv .\venv`

Depending on the tool you are using this might not open the virtual environment.
The virtual environment is open, if the command line feed starts with `(venv)`.

If you have already created the venv but have closed the session after the 
creation of the venv or the venv has not opened, you need to open the venv with
a command. Assuming a ps terminal, this can be done with the following command (make 
sure powershell has the right to run scripts):

`.\venv\Scripts\Activate.ps1`

Other terminals should use the activate script in the folder that corresponds with the terminal type.

After your terminal has `(venv)` on the left side of the line, you can install the requirements with

`pip install -r requirements.txt`

### Running the tests

The tests can be run with pytest in the root folder:

`pytest`

### Environment variables

The tests can be controlled with environment variables, the following variables are available:

- `SKIP_LONG` : Skip tests with long expected run time
- `POKEAPI_URL` : Change the url the tests are run against (see [Using the proxy](#using-the-proxy))

## Using the proxy

To not stress PokeAPI servers, we have decided to use a local caching
proxy server. The server is available in GitHub (https://github.com/EddieTheCubeHead/PokeapiProxyCache) and it's
usage is **highly** recommended if running the tests locally. Please see the instructions there for running the
server.

After the proxy cache is running, you can set the environment variable "POKEAPI_URL" to be "http://127.0.0.1:8000"
and the tests should use the proxy cache. Note that using "localhost" instead of "127.0.0.1" will often lead to
unnecessary DNS calls multiplying the time required for each request sent to the proxy.

**Please note that performance tests will likely fail if you are not using a "warm" cache** Warming up the cache
probably takes around 10(!) test runs and the first runs might be unbearably slow.