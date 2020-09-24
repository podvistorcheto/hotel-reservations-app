$(document).ready(function () {
    var minDate = new Date();
    $("#checks_in").datepicker({
        showAnim: 'drop',
        numberOfMonth: 1,
        minDate: minDate,
        dateFormat: 'dd/mm/yyyy',
        onClose: function (selectedDate) {
            $('#checks_out').datepicker("option", "minDate", selectedDate)
        }
    });
    $("#checks_out").datepicker({
        showAnim: 'drop',
        numberOfMonth: 1,
        minDate: minDate,
        dateFormat: 'dd/mm/yyyy',
        onClose: function (selectedDate) {
            $('#checks_out').datepicker("option", "minDate", selectedDate)
        }
    });
});