/***
 * App requirements
 */
const express = require("express");
const app = express();
const ROOT = __dirname + '/';

/**
 Enable environment variables
 */
require('dotenv').config();

/**
 * DB requirements
 */
require("./db");

/**
 * Enable cors platforms
 */
app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content, Accept, Content-Type, Authorization');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, PATCH, OPTIONS');
    next();
});


app.get('/api', (req, res) => {
    res.status(200).send('Comments API works');
});

const CommentController = require(ROOT + 'comment/CommentController');
app.use('/api/comments', CommentController);

module.exports = app;
