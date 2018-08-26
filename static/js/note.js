$(document).ready( function() {
  var currentDate = new Date()
  var tomorrowDate = new Date(currentDate)
  tomorrowDate.setDate(currentDate.getDate() + 1)
  var maxDate = new Date(currentDate)
  maxDate.setFullYear(maxDate.getFullYear() + 100)

  $('#starting_date').val(formatDate(currentDate))
  $("#starting_date")[0].setAttribute("min",formatDate(currentDate))
  $("#starting_date")[0].setAttribute("max",formatDate(maxDate))

  $('#ending_date').val(formatDate(tomorrowDate))
  $("#ending_date")[0].setAttribute("min",formatDate(tomorrowDate))
  $("#ending_date")[0].setAttribute("max",formatDate(maxDate))
})

function formatDate(date) {
  //YYYY-MM-DD
  var d = new Date(date),
      month = '' + (d.getMonth() + 1),
      day = '' + d.getDate(),
      year = d.getFullYear()

  if (month.length < 2) month = '0' + month
  if (day.length < 2) day = '0' + day

  return [year, month, day].join('-')
}

function onDateChange() {
  var startingDateStr = $("#starting_date").val()
  var endingDateStr = $("#ending_date").val()

  var startingDate = new Date(startingDateStr)
  var endingDate = new Date(endingDateStr)

  var newEndingDate = new Date(startingDate)
  newEndingDate.setDate(startingDate.getDate() + 1)

  if( startingDate.getTime() >= endingDate.getTime()) {
    $('#ending_date').val(formatDate(newEndingDate))
  }
  $("#ending_date")[0].setAttribute("min",formatDate(newEndingDate))
}