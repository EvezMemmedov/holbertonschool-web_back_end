const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if(err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data
        .split('\n')
        .filter((line) =>line.trim() !== '');

      const students = lines.slice(1);
      console.log(`Number of students: ${students.length}`);
      const fields = {};
      students.forEach((line) => {
        const parts = line.split(',');
        const firstName = parts[0];
        const field = parts[3];
      if(!fields[filed]) {
        fields[field] = [];
      }
      fileds[filed].push(firstName);
      });
      Object.keys(fileds).forEach((filed) => {
        console.log(
          `Number of students in ${filed}: ${fileds[filed].length}. List: ${fileds[filed].join(', ')}`,
        );
      });
      resolve();
    });
  });
}
module.exports = countStudents;
