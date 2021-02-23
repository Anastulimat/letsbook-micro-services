/**
 * CommentController requirements
 */
const express = require("express");
const router = express.Router();
const bodyParser = require("body-parser");
router.use(bodyParser.urlencoded({ extended: false }));
router.use(bodyParser.json());

/**
 * Comment model
 */
let Comment = require('./Comment');

/**
 * Create a new comment
 */
router.post('/', (req, res) => {
    const newComment = new Comment({
        ...req.body
    });

    newComment.save()
        .then(() => res.status(201).json('Comment added !'))
        .catch((error) => res.status(500).json("There was a problem adding the information to the database. " + error));
});

/**
 * Get all comments related to a book
 */
router.get('/:book_id', (req, res) => {
    Comment.find({book_id: req.params.book_id})
        .then((comments) => res.status(200).json(comments))
        .catch((error) => res.status(500).json("There was a problem finding the related comments. " + error));
});

/**
 * Update a comment
 */
router.put('/:id', (req, res) => {
   Comment.updateOne({_id:req.params.id}, { ...req.body, _id: req.params.id })
       .then(() => res.status(200).json("Comment was updated !"))
       .catch((error) => res.status(500).json("There was a problem updating the comment. " + error));
});

/**
 * Delete a comment from the database
 */
router.delete('/:id', (req, res) => {
    Comment.deleteOne({_id:req.params.id})
        .then(() => res.status(200).json("Comment was deleted !"))
        .catch((error) => res.status(200).json("There was a problem deleting the comment. " + error));
});


module.exports = router;
