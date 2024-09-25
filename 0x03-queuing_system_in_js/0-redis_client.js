const {createClient} = require('redis');

const client = createClient();

client.on('connect', function() {
    console.log('Redis client connected to the server');
});

client.on('error', (err) =>
    console.log('Redis client not connected to the server:', err));

client.connect();