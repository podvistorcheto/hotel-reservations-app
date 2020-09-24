$(function () {
    $.datepicker.setDefaults({
        minDate: new Date(),
    });
    $("#checks_in").datepicker({
        onSelect: function (selectedDate) {
            var date = $(this).datepicker("getDate");
            if (date) {
                date.setDate(date.getDate() + 1);
            }
            $("#checks_out").datepicker("option", "minDate", date || new Date());
        },
    });
    $("#checks_out").datepicker({
        onSelect: function (selectedDate) {
            var date = $(this).datepicker("getDate");
            if (date) {
                date.setDate(date.getDate() - 1);
            }
            $("#checks_in").datepicker("option", "maxDate", date);
        },
    });
});