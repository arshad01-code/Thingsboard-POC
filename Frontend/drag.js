function enableDrag(element){
  element.onmousedown = function(e){
    let shiftX = e.clientX - element.getBoundingClientRect().left;
    let shiftY = e.clientY - element.getBoundingClientRect().top;

    function moveAt(pageX,pageY){
      element.style.position='absolute';
      element.style.left = pageX - shiftX + 'px';
      element.style.top = pageY - shiftY + 'px';
    }

    function onMouseMove(e){
      moveAt(e.pageX,e.pageY);
    }

    document.addEventListener('mousemove',onMouseMove);

    element.onmouseup = function(){
      document.removeEventListener('mousemove',onMouseMove);
    };
  };
}