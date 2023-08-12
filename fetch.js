import axios from 'axios';

const url = 'http://127.0.0.1:5000/predict';
const data = { symptoms: ['headache', 'nausea', 'vomiting', 'fatigue', 'mood swings', 'neck pain', 'dizziness'] };

axios.post(url, data)
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error('Error:', error);
  });
