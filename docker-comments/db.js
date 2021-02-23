/**
 * MongoDB connexion settings
 */
const mongoose = require('mongoose');
const mongodb_comments_uri = process.env.MONGODB_COMMENTS_URI;

mongoose.connect(mongodb_comments_uri, {
    useNewUrlParser: true,
    useCreateIndex: true ,
    useUnifiedTopology: true})
    .then(() => console.log("MongoDB database connection established successfully !"))
    .catch((error) => console.log("MongoDB database has crashed !" + error));
