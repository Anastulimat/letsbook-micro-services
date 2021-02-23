const mongoose = require('mongoose');

const CommentSchema = new mongoose.Schema(
    {
        user_id : {type: String, required: true},
        book_id: {type: String, required: true},
        content: {type: String, required: true},
        date: {type: Date, required: false},
    },
    {
        timestamps: true
    }
);

const Comment = mongoose.model('Comment', CommentSchema);

module.exports = Comment;
