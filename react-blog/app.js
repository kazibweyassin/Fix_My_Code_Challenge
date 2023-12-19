/**
 * Express configurations.
 */

import { Router } from 'react-router';
import React from 'react';
import express from 'express';
import Iso from 'iso';
import session from 'express-session';
import path from 'path';
import bodyParser from 'body-parser';
import cookieParser from 'cookie-parser';

//Define Routes here
import posts from './routes/post.routes';
import routes from './src/routes.jsx';
import alt from './src/alt';
import config from './config.js';

const app = express();

app.set('views', __dirname+'/views');
app.set('view engine', 'jade');

app.use(express.static(path.join(__dirname, 'public')));
app.use(session({secret: 'copy cat', resave: false, saveUninitialized: true}));
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json({limit : '50mb'}));
app.use(cookieParser());

//use Routes here
app.use('/',posts);

app.use(function (req, res) {

    var data = res.locals.data || {};
    alt.bootstrap(JSON.stringify(data));
    
    var metaDescription = res.locals.metaDescription || '';

    var iso = new Iso();

    Router.run(routes, req.url, function (Handler) {

        var content = React.renderToString(React.createElement(Handler));

        iso.add(content, alt.flush());
        
        res.render('index',{
            content:iso.render(),
            pageTitle: config.pageTitle,
            metaDescription: metaDescription
        });
    });
});

// production error handler
// no stacktraces leaked to user
app.use(function(err, req, res) {

    if(!err.status || err.status !== 404){
        err.status = 500;
    }

    console.log(err);

    res.status(err.status);

    res.sendFile(path.resolve(__dirname+'/views/error/'+err.status+'.html'));

});

app.listen(config.port, function () {
    console.log('Listening on ' + config.baseUrl);
});