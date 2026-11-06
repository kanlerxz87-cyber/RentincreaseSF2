
document.addEventListener('DOMContentLoaded',function(){
  document.querySelectorAll('input[data-filter]').forEach(function(inp){
    var tid=inp.getAttribute('data-filter');
    var tbl=document.getElementById(tid); if(!tbl) return;
    var rows=Array.prototype.slice.call(tbl.querySelectorAll('tbody tr'));
    var cnt=document.getElementById(tid+'-count');
    inp.addEventListener('input',function(){
      var q=inp.value.trim().toLowerCase(),n=0;
      rows.forEach(function(r){
        var hit=!q||r.textContent.toLowerCase().indexOf(q)>=0;
        r.style.display=hit?'':'none'; if(hit)n++;
      });
      if(cnt)cnt.textContent=n+' of '+rows.length+' rows';
    });
    if(cnt)cnt.textContent=rows.length+' of '+rows.length+' rows';
  });
  document.querySelectorAll('[data-sev]').forEach(function(b){
    b.addEventListener('click',function(){
      var s=b.getAttribute('data-sev');
      var on=!b.classList.contains('on');
      document.querySelectorAll('[data-sev]').forEach(function(x){x.classList.remove('on')});
      if(on)b.classList.add('on');
      var t=document.getElementById(b.getAttribute('data-target')); if(!t)return;
      t.querySelectorAll('tbody tr').forEach(function(r){
        r.style.display=(!on||r.getAttribute('data-sev')===s)?'':'none';
      });
    });
  });
});
