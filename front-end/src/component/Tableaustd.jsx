import { useState, useEffect } from 'react';
import axios from 'axios';

const ScheduleTablestd = () => {
  const [scheduleData, setScheduleData] = useState([]);

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

  // Créer un tableau 2D pour stocker les données par jour et groupe
  const scheduleByDayAndGroup = {};

  // Organiser les données par jour et groupe
  scheduleData.forEach(item => {
    if (!scheduleByDayAndGroup[item.day]) {
      scheduleByDayAndGroup[item.day] = {};
    }
    if (!scheduleByDayAndGroup[item.day][item.group_name]) {
      scheduleByDayAndGroup[item.day][item.group_name] = [];
    }
    scheduleByDayAndGroup[item.day][item.group_name].push(item);
  });

  return (
    <div className="container mx-auto">
      <h2 className="text-2xl font-bold mb-4">Schedule</h2>
      <div className="overflow-x-auto">
        <table className="min-w-full">
        <thead>
  <tr>
    <th className="border border-neutral-700 px-4 py-2">Day/Group</th>
    {scheduleByDayAndGroup['Monday'] !== undefined && Object.keys(scheduleByDayAndGroup['Monday']).map(group => (
      <th key={group} className="border border-neutral-700 px-4 py-2">{group}</th>
    ))}
  </tr>
</thead>
          <tbody>
            {/* Parcourir les jours et afficher les données par jour et groupe */}
            {Object.keys(scheduleByDayAndGroup).map(day => (
              <tr key={day}>
                <td className="border border-neutral-700 px-4 py-2">{day}</td>
                {Object.keys(scheduleByDayAndGroup[day]).map(group => (
                  <td key={group} className="border border-neutral-700 px-4 py-2">
                  {scheduleByDayAndGroup[day][group] &&
    scheduleByDayAndGroup[day][group].slice(0, 3).map(item => (
        <div key={item.id}>
            <p><strong>Module:</strong> {item.module_name}</p>
            <p><strong>Teacher:</strong> {item.teacher_name}</p>
            <p><strong>Time:</strong> {item.start_time}</p>
            <p><strong>Classroom:</strong> {item.classroom_name}</p>
            <hr className='border-neutral-700'/>
        </div>
    ))}

                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default ScheduleTablestd;
