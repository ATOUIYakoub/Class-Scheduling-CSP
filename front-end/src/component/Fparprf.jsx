import { useState, useEffect } from 'react';
import axios from 'axios';

const ScheduleTablestdP = () => {
  const [scheduleData, setScheduleData] = useState([]);
  const [teachers, setTeachers] = useState([]);
  const [days, setDays] = useState([]);
  const [selectedTeacher, setSelectedTeacher] = useState('');
  const [selectedDay, setSelectedDay] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/API/TimeTable/');
        setScheduleData(response.data);

        // Récupérer la liste des enseignants distincts
        const uniqueTeachers = [...new Set(response.data.map(item => item.teacher_name))];
        setTeachers(uniqueTeachers);

        // Récupérer la liste des jours distincts
        const uniqueDays = [...new Set(response.data.map(item => item.day))];
        setDays(uniqueDays);
      } catch (error) {
        console.error('Error fetching schedule data:', error);
      }
    };

    fetchData();
  }, []);

  // Filtrer les données par enseignant et par jour
  const filteredScheduleByTeacherAndDay = () => {
    let filteredSchedule = scheduleData;
    if (selectedTeacher !== '') {
      filteredSchedule = filteredSchedule.filter(item => item.teacher_name === selectedTeacher);
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
        {/* Sélecteur pour filtrer par enseignant */}
        <select value={selectedTeacher} onChange={e => setSelectedTeacher(e.target.value)}>
          <option value="">Select Teacher</option>
          {teachers.map(teacher => (
            <option key={teacher} value={teacher}>{teacher}</option>
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
              <th className="border px-4 py-2">Teacher/Day</th>
              {days.map(day => (
                <th key={day} className="border px-4 py-2">{day}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            <tr>
              <td className="border px-4 py-2">{selectedTeacher}</td>
              {days.map(day => (
                <td key={day} className="border px-4 py-2">
                  {filteredScheduleByTeacherAndDay().map(item => (
                    (item.teacher_name === selectedTeacher && item.day === day) &&
                    <div key={item.id}>
                      <p><strong>Module:</strong> {item.module_name}</p>
                      <p><strong>Group:</strong> {item.group_name}</p>
                      <p><strong>Time:</strong> {item.start_time}</p>
                      <p><strong>Classroom:</strong> {item.classroom_name}</p>
                    </div>
                  ))}
                </td>
              ))}
            </tr>
          </tbody>

        </table>
      </div>
    </div>
  );
}

export default ScheduleTablestdP;
