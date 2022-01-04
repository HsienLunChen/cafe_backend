
const express = require("express");

const PORT = process.env.PORT || 3001;

const app = express();
const path = require('path');
const sqlite3 = require('sqlite3');
const sqlite = require('sqlite');

const SERVER_ERROR = 500;
const REQ_ERROR = 400;

const SERVER_ERROR_MSG = "Internal Server Error";
const CITY__DISTRICT_MISSING_MSG = "City and district parameter missing";
const MRT_MISSING_MSG = "Mrt missing";
const ORDER_MISSING_MSG = "Order missing";
const WEEKDAY_MISSING_MSG = "Weekday missing";
const DETAIL_MISSING_MSG = "detail missing";

const days = {
  "Sun": {
    "open": "SunOpen",
    "close": "SunClose"
  },
  "Mon": {
    "open": "MonOpen",
    "close": "MonClose"
  },
  "Tue": {
    "open": "TueOpen",
    "close": "TueClose"
  },
  "Wen": {
    "open": "WenOpen",
    "close": "WenClose"
  },
  "Thu": {
    "open": "ThuOpen",
    "close": "ThuClose"
  },
  "Fri": {
    "open": "FriOpen",
    "close": "FriClose"
  },
  "Sat": {
    "open": "SatOpen",
    "close": "SatClose"
  }
}


app.use(express.static(path.resolve(__dirname, '../client/build')));

app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});

app.get("/cafe/city", async function(req, res) {
  try {
    console.log("requesting");
    let city = req.query.city;
    let district = req.query.district;
    let order = req.query.order;
    let weekday = req.query.weekday;

    if (!city) {
      res.type('text');
      res.status(REQ_ERROR).send(CITY__DISTRICT_MISSING_MSG);
    } else if (!order) {
      res.type('text');
      res.status(REQ_ERROR).send(ORDER_MISSING_MSG);
    } else if (!weekday) {
      res.type('text');
      res.status(REQ_ERROR).send(WEEKDAY_MISSING_MSG);
    } else if (!req.query.detail) {
      res.type('text');
      res.status(REQ_ERROR).send(DETAIL_MISSING_MSG);
    } else {
      let db = await getDB();
      let result;
      let query = "Select * from CAFES";
      let whereClause = " Where city=? ";
      let orderClause =" ORDER BY " + order + " DESC;";
      if (req.query.detail === 'no') {
        if (district) whereClause += "and district='"+ district + "'";
        result = await db.all(query, city);
      } else {
        if (district) whereClause += "and district='"+ district + "'";
        let wifi = req.query.wifi;
        let limitedTime = req.query.limited_Time;
        let quiet = req.query.quiet;
        let socket = req.query.socket;
        if (quiet === '1') {
          whereClause += " and quiet>=3 ";
        } else if (quiet === '2') {
          whereClause += " and quiet<3 and quiet > 1 ";
        } else if (quiet === '3'){
          whereClause += " and quiet<=1 ";
        } else {
          whereClause += " and quiet>=0 ";
        }
        if (limitedTime && limitedTime === 'yes') whereClause += " and (limited_time='no' OR limited_time='maybe') ";
        if (wifi && wifi === 'yes') whereClause += " and wifi>=1 ";
        if (socket && socket === 'yes') whereClause += " and (socket='yes' OR socket='maybe') ";

        if (req.query.now && req.query.now !== 'no') {
          let now = req.query.now;
          whereClause += " and " + days[weekday]['open'] + "<" + now + " and " + days[weekday]['close'] + ">" + now + " ";

        } else if (req.query.start && req.query.start !== 'no') {
          let start = req.query.start;
          let end = req.query.end;
          whereClause += " and " + days[weekday]['open'] + "<" + start + " and " + days[weekday]['close'] + ">" + end + " ";
        }
        query += (whereClause + orderClause);
        console.log(query);
        result = await db.all(query, city);
        console.log("with detail");
      }
      res.json(result);
    }
  } catch (err) {
    res.type("text");
    console.error(err);
    res.status(SERVER_ERROR).send(err);
  }
})

app.get("/cafe", async function(req, res) {
  try {
    console.log("requesting");
    let order = req.query.order;
    let weekday = req.query.weekday;

    if (!order) {
      res.type('text');
      res.status(REQ_ERROR).send(ORDER_MISSING_MSG);
    } else if (!weekday) {
      res.type('text');
      res.status(REQ_ERROR).send(WEEKDAY_MISSING_MSG);
    } else if (!req.query.detail) {
      res.type('text');
      res.status(REQ_ERROR).send(DETAIL_MISSING_MSG);
    } else {
      let db = await getDB();
      let result;
      let query = "Select * from CAFES";
      let whereClause = " Where ";
      let orderClause =" ORDER BY " + order + " DESC;";
      if (req.query.detail === 'no') {
        query += (orderClause);
        console.log(query);
        result = await db.all(query);
      } else {
        let wifi = req.query.wifi;
        let limitedTime = req.query.limited_Time;
        let quiet = req.query.quiet;
        let socket = req.query.socket;
        if (quiet === '1') {
          whereClause += "quiet>=3";
        } else if (quiet === '2') {
          whereClause += "quiet<3 and quiet > 1";
        } else if (quiet === '3'){
          whereClause += "quiet<=1";
        } else {
          whereClause += "quiet>=0";
        }
        if (limitedTime && limitedTime === 'yes') whereClause += " and (limited_time='no' OR limited_time='maybe') ";
        if (wifi && wifi === 'yes') whereClause += " and wifi>=1 ";
        if (socket && socket === 'yes') whereClause += " and (socket='yes' OR socket='maybe') ";

        if (req.query.now && req.query.now !== 'no') {
          let now = req.query.now;
          whereClause += " and " + days[weekday]['open'] + "<" + now + " and " + days[weekday]['close'] + ">" + now + " ";

        } else if (req.query.start && req.query.start !== 'no') {
          let start = req.query.start;
          let end = req.query.end;
          whereClause += " and " + days[weekday]['open'] + "<" + start + " and " + days[weekday]['close'] + ">" + end + " ";
        }
        query += (whereClause + orderClause);
        console.log(query);
        result = await db.all(query);
        console.log("with detail");
      }
      res.json(result);
    }
  } catch (err) {
    res.type("text");
    console.error(err);
    res.status(SERVER_ERROR).send(err);
  }
})

app.get("/cafe/mrt", async function(req, res) {
  try {
    console.log("requesting");
    let mrt = req.query.mrt;
    let weekday = req.query.weekday;
    let order = req.query.order;
    let db = await getDB();
    let result;

    if (!mrt) {
      res.type('text');
      res.status(REQ_ERROR).send(MRT_MISSING_MSG);
    } else if (!order) {
      res.type('text');
      res.status(REQ_ERROR).send(ORDER_MISSING_MSG);
    } else if (!weekday) {
      res.type('text');
      res.status(REQ_ERROR).send(WEEKDAY_MISSING_MSG);
    } else if (!req.query.detail) {
      res.type('text');
      res.status(REQ_ERROR).send(DETAIL_MISSING_MSG);
    } else {
      let query = "Select * from CAFES ";
      let whereClause = "Where mrt=? ";
      let orderClause = "ORDER BY " + order + " DESC;";
      if (req.query.detail === 'no') {
        query += (whereClause + orderClause);
        console.log(query);
        result = await db.all(query, mrt);
      } else {
        let wifi = req.query.wifi;
        let limitedTime = req.query.limited_Time;
        let quiet = req.query.quiet;
        let socket = req.query.socket;

        if (limitedTime && limitedTime === 'yes') whereClause += " and (limited_time='no' OR limited_time='maybe') ";
        if (wifi && wifi === 'yes') whereClause += " and wifi>=1 ";
        if (socket && socket === 'yes') whereClause += " and (socket='yes' OR socket='maybe') ";
        console.log(quiet);
        if (quiet === '1') {
          whereClause += " and quiet>=3 ";
        } else if (quiet === '2') {
          whereClause += " and quiet<3 and quiet > 1 ";
        } else if (quiet === '3'){
          whereClause += " and quiet<=1 ";
        } else {
          whereClause += " and quiet>=0 ";
        }

        if (req.query.now && req.query.now !== 'no') {
          let now = req.query.now;
          whereClause += " and " + days[weekday]['open'] + "<" + now + " and " + days[weekday]['close'] + ">" + now + " ";

        } else if (req.query.start && req.query.start !== 'no') {
          let start = req.query.start;
          let end = req.query.end;
          whereClause += " and " + days[weekday]['open'] + "<" + start + " and " + days[weekday]['close'] + ">" + end + " ";
        }
        query += (whereClause + orderClause);
        console.log(query);
        result = await db.all(query, mrt);
        console.log("with detail");
      }
      res.json(result);
    }
  } catch (err) {
    res.type("text");
    console.error(err);

    res.status(SERVER_ERROR).send(SERVER_ERROR_MSG);
  }
})


async function getDB() {
  const db = await sqlite.open({
    filename: 'server/database.db',
    driver: sqlite3.Database
  });
  return db;
}

