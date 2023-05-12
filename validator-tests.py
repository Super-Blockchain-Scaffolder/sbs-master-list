
# Pass in objects with extra keys -> expect 'unexpected key not in schema' eror

# Pass is perfectly valid objects -> expect all good, tests pass

# Pass in object with key missing (each key in its own test) -> expect 'missing required key' error

# Types

- expect "name" to be a string

- expect "starter templates" to be an array of "StarterTemplate" objects

- expect each "StarterTemplate" to have...

    - "name" field that is a string
    - "repo-url" field that is a string
    - "live-url" field that is a string
    - "description" field that is a string
    
    - "maintainers" field that is an array of strings
    - "tags" field that is an array of strings