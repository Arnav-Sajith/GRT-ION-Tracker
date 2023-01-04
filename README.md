# GRT-ION-Tracker
This is a small Python Project made so I can see when the next ION leaves from a ION Station in Kitchener-Waterloo.

Instructions for use:

1. Sign up for a Google Maps API key. This is needed to run the program. API keys can be acquired following this guide:         https://developers.google.com/maps/documentation/javascript/get-api-key

2. Install the Python Google Maps API Library:
~~~
pip install googlemaps
~~~

3. Install the Python DotEnv Library
~~~
pip install python-dotenv
~~~

4. Fill in the values in the included .env file with your API Key and desired ION stop
~~~
API_KEY = "Insert Google Maps API Key here without quotation marks"
ION_STOP = "Insert desired ION stop here without quotation marks"
~~~
Should become something like this:
~~~
API_KEY = ABCDEFG12345
ION_STOP = Conestoga Mall Station, Waterloo, Ontario, Canada
~~~

5. Run the main.py file
