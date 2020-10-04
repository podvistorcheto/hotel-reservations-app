$(function () {
    $.datepicker.setDefaults({
        minDate: new Date(),
    });
    $("#id_date_started").datepicker({
        onSelect: function (selectedDate) {
            var date = $(this).datepicker("getDate");
            if (date) {
                date.setDate(date.getDate() + 1);
            }
            $("#id_date_due").datepicker("option", "minDate", date || new Date());
        },
    });
    $("#id_date_due").datepicker({
        onSelect: function (selectedDate) {
            var date = $(this).datepicker("getDate");
            if (date) {
                date.setDate(date.getDate() - 1);
            }
            $("#id_date_started").datepicker("option", "maxDate", date);
        },
    });
});