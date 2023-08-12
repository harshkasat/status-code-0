const url = 'http://127.0.0.1:5000/predict';
const data = { symptoms: ['headache', 'nausea', 'vomiting', 'fatigue', 'mood swings', 'neck pain', 'dizziness'] };

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error('Fetch error:', error);
  });
