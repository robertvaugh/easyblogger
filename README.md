# Vim-Blogger

Blog to blogger with Vim.


## Why not googlecl?
I tried. Didn't work. `googlecl` is just too rough and isn't easy to script. For ex:

1. No way to update a post
2. Doesn't work with blog and post ids.
3. and others...

## So what does this do
Blogger integration is planned through `gdata-python-client` using gdata apis.


# Blogger.py

Sample call

~~~bash
python blogger.py 132424086208.apps.googleusercontent.com DKEk2rvDKGDAigx9q9jpkyqI 7642453

# param 1: API key
# param 2: API secret
# param 3: Blog Id - look at your blog's atom pub url - its the number in the url.
~~~

