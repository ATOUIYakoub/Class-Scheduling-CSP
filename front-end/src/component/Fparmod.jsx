import { useState, useEffect } from 'react';
import axios from 'axios';

const ScheduleTablestdm = () => {
  const [scheduleData, setScheduleData] = useState([]);
  const [selectedModule, setSelectedModule] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/API/TimeTable/');
        setScheduleData(response.data);
      } catch (error) {
        console.error('Error fetching schedule data:', error);
      }
    };

    fetchData();
  }, []);

  const handleModuleChange = (event) => {
    setSelectedModule(event.target.value);
  };

  return (
    <div>
      <h2>Schedule</h2>
      <div>
        <label htmlFor="module">Select a module:</label>
        <select id="module" onChange={handleModuleChange} value={selectedModule}>
          <option value="">All</option>
          {[...new Set(scheduleData.map(item => item.module_name))].map(module => (
            <option key={module} value={module}>{module}</option>
          ))}
        </select>
      </div>
      <ul>
        {scheduleData
          .filter(item => !selectedModule || item.module_name === selectedModule)
          .map((item, index) => (
            <li key={index}>
              <strong>Module:</strong> {item.module_name}, <strong>Teacher:</strong> {item.teacher_name}, <strong>Group:</strong> {item.group_name}, <strong>Classroom:</strong> {item.classroom_name}, <strong>Day:</strong> {item.day}, <strong>Time:</strong> {item.start_time}
            </li>
          ))}
      </ul>
    </div>
  );
}

export default ScheduleTablestdm;
