function addWidget(){
  const title = document.getElementById("title").value;
  const key = document.getElementById("key").value;
  const type = document.getElementById("type").value;

  const widget = {
    type,
    title,
    telemetryKey: key,
    x:0,y:0,w:3,h:2
  };

  widgets.push(widget);

  const div = document.createElement("div");
  div.className="widget";
  div.innerText = title;

  enableDrag(div);
  document.getElementById("canvas").appendChild(div);
}