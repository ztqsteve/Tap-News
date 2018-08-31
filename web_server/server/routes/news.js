var express = require('express');
var router = express.Router();

/* GET news listing. */
router.get('/', function(req, res, next) {
  news = [
    {
      url:'',
      title:'sdf',
      description:'sdf',
      source:'sdf',
      urlToImage:'',
      digest:'sdf',
      reason:'dsf'
    },{
      url:'',
      title:'sdf',
      description:'sdf',
      source:'sdf',
      urlToImage:'',
      digest:'dsf',
      time:'sdf',
      reason:'sdf'
    }
  ];
  res.json(news);
});

module.exports = router;
