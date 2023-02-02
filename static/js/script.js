if (localStorage.getItem('lsTest')) {
    alert(JSON.parse(localStorage.getItem('lsTest')).value);
  }
  
  document.querySelector('button').addEventListener('click', function() {
   const val = document.querySelector('textarea').value.trim();
    
    if (val) {
      const obj = {
        date: new Date(),
        type: 'education',
        value: val
      };
      
      localStorage.setItem('lsTest', JSON.stringify(obj));
    }
  }, false);