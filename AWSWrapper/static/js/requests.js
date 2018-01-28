function buttonAjax(buttonElem, options, failOnly) {
    if (failOnly === undefined) {
        failOnly = false;
    }

    // Get original html and click events
    var html = buttonElem.html();

    // Disable button
    buttonElem
        .prop('disabled', true)
        .css('pointer-events', 'none')
        .css('cursor', 'not-allowed');

    // Set spinner
    var icons = buttonElem.find('i.fa');
    if (icons.length > 0) {
        // Set icon to spinner
        var icon = $(icons[0]);
        icon.removeClass('fa-*');
        icon.addClass('fa-spinner fa-spin')
    } else {
        // Prepend spinner
        buttonElem.html('<i class="fa fa-spinner fa-spin"></i>&nbsp;' + html);
    }

    var disableFunc = function () {
        // Reset original html
        buttonElem.html(html);

        // Enable button
        buttonElem
            .css('pointer-events', '')
            .prop('disabled', false)
            .css('cursor', '');
    };

    // Send AJAX
    if (failOnly === true) {
        return $.ajax(options).always(fail);
    } else {
        return $.ajax(options).always(disableFunc);
    }
}

$(document).ready(function () {
    var instance = $('#my-data').data().name;
    console.log(instance);

    $('#buttonIAMRole').click(function (e) {
        buttonAjax($(this), {
            method: "POST",
            url: "/setIAMRole/" + instance,
            data: {

            },
            success: function (data, textStatus, request) {

            },
            error: function (data, textStatus, request) {

            }
        });
    });
    $('#buttonScaling').click(function (e) {				            
        buttonAjax($(this), {
            method: "POST",
            url: "/setScaling/" + instance,
            data: {

            },
            success: function (data, textStatus, request) {

            },
            error: function (data, textStatus, request) {

            }
        });
    });
    $('#buttonType').click(function (e) {
        buttonAjax($(this), {
            method: "POST",
            url: "/setType/" + instance,
            data: {

            },
            success: function (data, textStatus, request) {

            },
            error: function (data, textStatus, request) {

            }
        });
    });
    $('#buttonTermination').click(function (e) {
         buttonAjax($(this), {
            method: "POST",
            url: "/setTermination/" + instance,
            data: {

            },
            success: function (data, textStatus, request) {

            },
            error: function (data, textStatus, request) {

            }
        });
    });
    $('#buttonUserData').click(function (e) {
          buttonAjax($(this), {
            method: "POST",
            url: "/setUserData/" + instance,
            data: {

            },
            success: function (data, textStatus, request) {

            },
            error: function (data, textStatus, request) {

            }
        });
    });
    $('#buttonT2').click(function (e) {
           buttonAjax($(this), {
            method: "POST",
            url: "/setT2/" + instance,
            data: {

            },
            success: function (data, textStatus, request) {

            },
            error: function (data, textStatus, request) {

            }
        });
    });
    $('#buttonModifyInstance').click(function (e) {
            buttonAjax($(this), {
            method: "POST",
            url: "/setModifyInstance/" + instance,
            data: {

            },
            success: function (data, textStatus, request) {

            },
            error: function (data, textStatus, request) {

            }
        });
    });
    $('#buttonNewInstance').click(function (e) {
             buttonAjax($(this), {
            method: "POST",
            url: "/setNewInstance/" + instance,
            data: {

            },
            success: function (data, textStatus, request) {

            },
            error: function (data, textStatus, request) {

            }
        });
    });
    $('#buttonStart').click(function (e) {
         buttonAjax($(this), {
            method: "POST",
            url: "/setStart/" + instance,
            data: {

            },
            success: function (data, textStatus, request) {

            },
            error: function (data, textStatus, request) {

            }
        });
    });
    $('#buttonStop').click(function (e) {
         buttonAjax($(this), {
            method: "POST",
            url: "/setStop/" + instance,
            data: {

            },
            success: function (data, textStatus, request) {

            },
            error: function (data, textStatus, request) {

            }
        });
    });
    $('#buttonReboot').click(function (e) {
         buttonAjax($(this), {
            method: "POST",
            url: "/setReboot/" + instance,
            data: {

            },
            success: function (data, textStatus, request) {

            },
            error: function (data, textStatus, request) {

            }
        });
    });
    $('#buttonKill').click(function (e) {
         buttonAjax($(this), {
            method: "POST",
            url: "/setKill/" + instance,
            data: {

            },
            success: function (data, textStatus, request) {

            },
            error: function (data, textStatus, request) {

            }
        });
    });
    $('#dropDownCreateImage').click(function (e) {
         buttonAjax($(this), {
            method: "POST",
            url: "/setDownCreateImage/" + instance,
            data: {

            },
            success: function (data, textStatus, request) {

            },
            error: function (data, textStatus, request) {

            }
        });
    });
    $('#dropDownBundleInstance').click(function (e) {
         buttonAjax($(this), {
            method: "POST",
            url: "/setDownBundleInstance/" + instance,
            data: {

            },
            success: function (data, textStatus, request) {

            },
            error: function (data, textStatus, request) {

            }
        });
    });
});

