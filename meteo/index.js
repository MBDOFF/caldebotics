const express = require("express");
const fs = require("fs");
const csv = require("csv-parser");
const path = require("path");

const app = express();

app.get("/data", (req, res) => {
  const data = [];

  fs.createReadStream("data.txt")
    .pipe(csv())
    .on("data", (row) => {
      data.push(row);
    })
    .on("end", () => {
      const lastEntry = data[data.length - 1];
      const jsonData = {
        temperature: lastEntry.temperature,
        humidity: lastEntry.humidity,
        wind: lastEntry.wind,
        pressure: lastEntry.pressure,
      };

      res.json(jsonData);
    });
});

app.use(express.static(path.join(__dirname, "public")));

app.listen(3000, () => {
  console.log("Server started on port 3000");
});
