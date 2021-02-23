/***
 * Server requirements
 */
const app = require('./app');

/**
 * Port config
 */
const normalizePort = val => {
    const port = parseInt(val, 10);

    if(isNaN(port)) {
        return val;
    }
    if(port >= 0) {
        return port;
    }
    return false;
};

const port = normalizePort(process.env.PORT || '5001');
app.set('port', port);

app.listen(port, () => {
    console.log("Express server listening on port " + port);
});
