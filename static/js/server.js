const axios = require('axios');

const data = {
    time_start: new Date(),
    time_end: new Date(),
    tag: tagSelect.value,
    pomodoro_count: 2
};

axios.post('/api/add_session', {data})
    .then(response => {
        console.log(response.data.result);
    }
    )
    .catch(error => {
        console.log(error);
    }

    );
