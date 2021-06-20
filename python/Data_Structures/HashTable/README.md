[Pull request](https://github.com/Omar-zoubi/data-structures-and-algorithms/pull/40)

# Hashtables
<!-- Short summary or background information -->
New structural way to deal with data.
## Challenge
<!-- Description of the challenge -->
we need to write four function `add` `get` `contains` `hash` to create our hashtable.
## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Time: O(1)
Space: O(N)
## API
<!-- Description of each method publicly available in each of your hashtable -->

`add`: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
`get`: takes in the key and returns the value from the table.
`contains`: takes in the key and returns a boolean, indicating if the key exists in the table already.
`hash`: takes in an arbitrary key and returns an index in the collection.