import { useState, useEffect } from 'react';
import axios from 'axios';

const ScheduleTablestd = () => {
  const [scheduleData, setScheduleData] = useState([]);
  const [groups, setGroups] = useState([]);
  const [days, setDays] = useState([]);
  const [selectedGroup, setSelectedGroup] = useState('');
  const [selectedDay, setSelectedDay] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/API/TimeTable/');
        setScheduleData(response.data);

        // Récupérer la liste des groupes distincts
        const uniqueGroups = [...new Set(response.data.map(item => item.group_name))];
        setGroups(uniqueGroups);

        // Récupérer la liste des jours distincts
        const uniqueDays = [...new Set(response.data.map(item => item.day))];
        setDays(uniqueDays);
      } catch (error) {
        console.error('Error fetching schedule data:', error);
      }
    };

    fetchData();
  }, []);

  // Filtrer les données par groupe et par jour
  const filteredScheduleByGroupAndDay = () => {
    let filteredSchedule = scheduleData;
    if (selectedGroup !== '') {
      filteredSchedule = filteredSchedule.filter(item => item.group_name === selectedGroup);
    }
    if (selectedDay !== '') {
      filteredSchedule = filteredSchedule.filter(item => item.day === selectedDay);
    }
    return filteredSchedule;
  };

  return (
    <div className="container mx-auto">
      <h2 className="text-2xl font-bold mb-4">Schedule</h2>
      <div>
        {/* Sélecteur pour filtrer par groupe */}
        <select value={selectedGroup} onChange={e => setSelectedGroup(e.target.value)}>
          <option value="">All Groups</option>
          {groups.map(group => (
            <option key={group} value={group}>{group}</option>
          ))}
        </select>
        {/* Sélecteur pour filtrer par jour */}
        <select value={selectedDay} onChange={e => setSelectedDay(e.target.value)}>
          <option value="">Select Day</option>
          {days.map(day => (
            <option key={day} value={day}>{day}</option>
          ))}
        </select>
      </div>
      <div className="overflow-x-auto">
        <table className="min-w-full">
          <thead>
            <tr>
              <th className="border px-4 py-2">Group/Day</th>
              {days.map(day => (
                <th key={day} className="border px-4 py-2">{day}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {/* Afficher tous les groupes par défaut */}
            {groups.map(group => (
              <tr key={group}>
                <td className="border px-4 py-2">{group}</td>
                {/* Pour chaque jour, afficher les données pour ce groupe et ce jour */}
                {days.map(day => (
                  <td key={day} className="border px-4 py-2">
                    {filteredScheduleByGroupAndDay().map(item => (
                      (selectedGroup === '' || item.group_name === selectedGroup) && item.day === day &&
                      <div key={item.id}>
                                                <p><strong>Module:</strong> {item.id}</p>

                        <p><strong>Module:</strong> {item.module_name}</p>
                        <p><strong>Teacher:</strong> {item.teacher_name}</p>
                        <p><strong>Time:</strong> {item.start_time}</p>
                        <p><strong>Classroom:</strong> {item.classroom_name}</p>
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
