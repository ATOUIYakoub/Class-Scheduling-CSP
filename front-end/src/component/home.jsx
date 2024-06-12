const Home = () => {
    return (
      <div className="h-screen w-full justify-center items-center flex flex-col gap-5 ">
        <form className=" bg-gray-300 flex flex-col w-2/3 justify-center items-center rounded-xl h-[70vh] gap-5">
     <p className="poppins text-4xl">welcome</p>
     <div className="flex flex-row gap-2 items-center justify-center">
     <label>teacher name</label>
     <select className=" poppins text-base rounded-xl h-9 w-7/12">
        <option className=" rounded-t-lg">Select the teacher</option>
        <option>dr Djenadi</option>
        <option>dr Zenadji </option>
        <option>dr Lekehali</option>
        <option>dr Sahli</option>
        <option>dr Alkama</option>
        <option>dr Issadi</option>
        <option>dr Zedek</option>
     </select>
     </div>
     <div className="flex flex-row  justify-around w-full p-2">
      <div className="flex flex-col gap-3 w-[42%]">
     <div className="flex flex-row gap-2 items-center justify-between">
     <label>day</label>
     <select className="  poppins text-base rounded-xl h-9 w-7/12">
        <option className=" rounded-t-lg">Select the day </option>
        <option>Sunday</option>
        <option>Monday</option>
        <option>Tuesday</option>
        <option>Wednesday</option>
        <option>Thursday</option>
     </select>
     </div>
     <div className="flex flex-row gap-2 items-center justify-between">
     <label>Select first time</label>
     <select className="  poppins text-base rounded-xl h-9 w-7/12">
     <option className=" rounded-t-lg">Select first time</option>
        <option>1</option>
        <option>2</option>
        <option>3</option>
        <option>4</option>
        <option>5</option>
     </select>
     </div>
     <div className="flex flex-row  justify-between">
     <label>Select second time</label>
     <select className=" poppins text-base rounded-xl h-9 w-7/12">
     <option className=" rounded-t-lg">Select second time</option>
        <option>1</option>
        <option>2</option>
        <option>3</option>
        <option>4</option>
        <option>5</option>
     </select>
     </div><div className="flex flex-row justify-between">
     <label>Select third time</label>
     <select className=" poppins text-base rounded-xl h-9 w-7/12">
     <option className=" rounded-t-lg">Select third time</option>
        <option>1</option>
        <option>2</option>
        <option>3</option>
        <option>4</option>
        <option>5</option>
     </select>
     </div>
     </div>
     <div className="flex flex-col gap-3 w-[42%]">
     <div className="flex flex-row gap-2 items-center justify-between">
     <label>day</label>
     <select className="  poppins text-base rounded-xl h-9 w-7/12">
        <option className=" rounded-t-lg">Select the day </option>
        <option>Sunday</option>
        <option>Monday</option>
        <option>Tuesday</option>
        <option>Wednesday</option>
        <option>Thursday</option>

     </select>
     </div>
     <div className="flex flex-row gap-2 items-center justify-between">
     <label>Select first time</label>
     <select className="  poppins text-base rounded-xl h-9 w-7/12">
     <option className=" rounded-t-lg">Select first time</option>
        <option>1</option>
        <option>2</option>
        <option>3</option>
        <option>4</option>
        <option>5</option>
     </select>
     </div>
     <div className="flex flex-row  justify-between">
     <label>Select second time</label>
     <select className=" poppins text-base rounded-xl h-9 w-7/12">
     <option className=" rounded-t-lg">Select second time</option>
        <option>1</option>
        <option>2</option>
        <option>3</option>
        <option>4</option>
        <option>5</option>
     </select>
     </div><div className="flex flex-row justify-between">
     <label>Select third time</label>
     <select className=" poppins text-base rounded-xl h-9 w-7/12">
     <option className=" rounded-t-lg">Select third time</option>
        <option>1</option>
        <option>2</option>
        <option>3</option>
        <option>4</option>
        <option>5</option>
     </select>
     </div>
     </div>
     </div>
     <button className="w-36 bg-red-600 text-white h-8 rounded-lg">clicker</button>
</form>
      </div>
    );
  }
  
  export default Home;
  