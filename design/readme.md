# Object-Oriented Design

Notes built on top of Cracking the Code

## How to Approach
Remember, don't try and waste time finding the 'right' pattern, there are always loads of ways to consider and model software. Need to just figure out how to model with something that is maintainable and also works!

### 1) Handle Ambiguity
- Need to spend time clarifying assumptions and asking client for more information.
- Ask all about who/how this is going to be used, this will massively reflect the way in which you design something.

### 2) Define the Core Objects
- E.G. designing a Cafe, core objects might be Barista, Table, Order etc.

### 3) Analyse Relationships
- Which objects are members of other objects? How are they related? One to Many? Many-to-One?
- Incorrect assumptions will lead to incorrect relationship modelling.

### 4) Investigate Actions
- Consider how objects will interact with each other in different scenarios.

A couple of the most common patterns are Singleton and Factory Method, make sure to internalise these.

## System Design and Scalability

This is something that has to be done by soliciting requirements from the interviewer, and isn't generally something to super prepare for, general concepts are useful though. I'm bullet pointing thse below:

### Horizontal vs Vertical Scaling
- Vertical scaling involves increasing the capacity of a given node, rather than the number of nodes. In general easier, but limited in potential scope.

### Load Balancer
- Placed infront of a client facing service, to distribute tasks as well as stop the potential of user induced crashing of servers.

### Database Denormalisation and NoSQL
- Denormalisation = storing redundant data with a given table to reduce needs for joins between tables storing semantically different information.

### Database Partitioning (Sharding)
Splitting data across multiple machines
- Vertical Partitioning: i.e. partitioning data by feature, i.e. one shard for user birthdates, another for addresses
- Key-Based (or Hash-Based) Partitioning: Uses some aspect of data to partition.
- Directory-Based Partitioning: maintain lookup table of where data can be found. This table is a single point of failure, and accessing the table impacts performance.

### Caching
- In-memory cache can rapidly speed up data retrieval. Generally a key-value store that sits in between an application layer and a data store.
- When an application seeks info, it will first look in here before checking data-store.

### Async Processing + Queues
- Ideally all quite slow operations should be done async.

### Newtorking Metrics
- Bandwidth: The max amount of data transferred per unit time units bits/s
- Throughput: Actual amount of data transferred
- Latency: Delay between sending and receiving.

### MapReduce
- Map takes some data producing a key, value pair.
- Reduce takes a key and a set of associated values and reduces shtme in some way.
- Allows for the parallelisation of tasks - especially data processing tasks.
