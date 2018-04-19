var daysleft = 0;
var today = moment().startOf('day');
dd = today.date();
mm = today.month() + 1;

function lastday(dd, mm) {
  if (dd == 23) {
    if (mm == 5) {
      return true;
    }
  }
  return false;
}

while (!lastday(dd, mm)) {
  today = today.add(1, 'days');
  dd = today.date();
  mm = today.month() + 1;
  w = today.isoWeekday();
  // weekends
  if (!(w == 7 || w == 6)) {
    daysleft++;
  }
}

document.getElementById("num").innerHTML = daysleft;