
function slideonlyone(ind) {
    table.rows('#mac' + ind).deselect();
    $('#kupondata' + ind).remove();

    var macs = table.rows(".selected").data().pluck(0).toArray().length;
    if (macs >= 1) {
        $('#kuponyap').click();
    } else {
       $("#nullcoupon").show();
       $("#kuponbilgileri").hide();
       $("#kuponbilgileritaban").hide();
       $("#macsayisi").html('0');

    }
}

function calculatedata(oddsp, analysis, macsayisi) {

    kellyp = (((oddsp * analysis - 1) / (oddsp - 1))*0.5).toFixed(2);

    if (parseFloat(kellyp).toFixed(2) > 0) {
        $("#kellyproduct").html(parseFloat(kellyp).toFixed(2));
    } else {
        $("#kellyproduct").html("<b>OYNAMA</b>");
    }
    $("#analysisproduct").html("%" + parseFloat(100 * analysis).toFixed(2));
    $("#oddproduct").html(parseFloat(oddsp).toFixed(2));

    $("#macsayisi").html(macsayisi);

}

function recalculateDataTableResponsiveSize() {
    $($.fn.dataTable.tables(true)).DataTable().columns.adjust().responsive.recalc();
}

$( window ).resize(function() {
  //recalculateDataTableResponsiveSize();
});


$(document).ready(function() {


(function blink() {
  $('.blinking').fadeOut(500).fadeIn(500, blink);
})();

$('a[data-toggle="tab"]').on('click', function(e) {
e.preventDefault();
$(this).tab('show');
var theThis = $(this);
$('a[data-toggle="tab"]').removeClass('active');
theThis.addClass('active');
});




    table = $("#tableRegister").DataTable({

        rowReorder: {
            selector: 'td:nth-child(1)'
        },
        responsive: true,
        language: {
            sDecimal: ",",
            sEmptyTable: "Tabloda herhangi bir veri mevcut değil",
            sInfo: "_TOTAL_ kayıttan _START_ - _END_ arasındaki kayıtlar gösteriliyor",
            sInfoEmpty: "Kayıt yok",
            sInfoFiltered: "(_MAX_ kayıt içerisinden bulunan)",
            sInfoPostFix: "",
            sInfoThousands: ".",
            sLengthMenu: "Sayfada _MENU_ kayıt göster",
            sLoadingRecords: "Yükleniyor...",
            sProcessing: "İşleniyor...",
            sSearch: "Ara:",
            sZeroRecords: "Eşleşen kayıt bulunamadı",
            oPaginate: {
                sFirst: "İlk",
                sLast: "Son",
                sNext: "Sonraki",
                sPrevious: "Önceki"
            },
            oAria: {
                sSortAscending: ": artan sütun sıralamasını aktifleştir",
                sSortDescending: ": azalan sütun sıralamasını aktifleştir"
            },
            select: {
                rows: {
                    _: "%d kayıt seçildi",
                    "0": "",
                    "1": "1 kayıt seçildi"
                }
            }
        },
        columnDefs: [


                { responsivePriority: 1, targets: 1 },
                { responsivePriority: 2, targets: 4 },
                { responsivePriority: 3, targets: 3 },
                { responsivePriority: 4, targets: 5 },
                { responsivePriority: 5, targets: 8 },
                { responsivePriority: 6, targets: 7 },
                { responsivePriority: 7, targets: 6 },
                { responsivePriority: 8, targets: 2 },

        {
                targets: [0],
                visible: false,
                searchable: false
            },
            {
                target: 4, //index of column
                type: "datetime-moment"
            }
        ],

        order: [
            [4, "asc"],
            [8, "desc"]
        ],

        orderCellsTop: true,
        fixedHeader: true
    });


    $.fn.dataTable.moment("DD/MM/YYYY HH:mm");

    tablebiten = $("#tableRegister2").DataTable({
        "createdRow": function(row, data, dataIndex) {
            if (data[9] == "0") {
                $(row).find("td").last().addClass('redClass');
                $(row).addClass('fail');
            }
            if (data[9] == "1") {
                $(row).find("td").last().addClass('greenClass');
                $(row).addClass('fail');
            }
        },
                rowReorder: {
            selector: 'td:nth-child(4)'
        },
        responsive: true,
        language: {
            sDecimal: ",",
            sEmptyTable: "Tabloda herhangi bir veri mevcut değil",
            sInfo: "_TOTAL_ kayıttan _START_ - _END_ arasındaki kayıtlar gösteriliyor",
            sInfoEmpty: "Kayıt yok",
            sInfoFiltered: "(_MAX_ kayıt içerisinden bulunan)",
            sInfoPostFix: "",
            sInfoThousands: ".",
            sLengthMenu: "Sayfada _MENU_ kayıt göster",
            sLoadingRecords: "Yükleniyor...",
            sProcessing: "İşleniyor...",
            sSearch: "Ara:",
            sZeroRecords: "Eşleşen kayıt bulunamadı",
            oPaginate: {
                sFirst: "İlk",
                sLast: "Son",
                sNext: "Sonraki",
                sPrevious: "Önceki"
            },
            oAria: {
                sSortAscending: ": artan sütun sıralamasını aktifleştir",
                sSortDescending: ": azalan sütun sıralamasını aktifleştir"
            },
            select: {
                rows: {
                    _: "%d kayıt seçildi",
                    "0": "",
                    "1": "1 kayıt seçildi"
                }
            }
        },
        columnDefs: [{
                targets: [0, 9],
                visible: false,
                searchable: false
            },
            {
                target: 4, //index of column
                type: "datetime-moment"
            }
        ],

        order: [
            [4, "desc"],
            [9, "desc"]
        ],

        orderCellsTop: true,
        fixedHeader: true
    });

    $.fn.dataTable.moment("DD/MM/YYYY HH:mm");

    tablecanli = $("#tableRegister3").DataTable({

              "createdRow": function(row, data, dataIndex) {
            if (data[10] == "0") {
                $(row).find("td").last().addClass('redClass');
                $(row).addClass('fail');
            }
            if (data[10] == "1") {
                $(row).find("td").last().addClass('greenClass');
                $(row).addClass('fail');
            }
        },
                                   rowReorder: {
            selector: 'td:nth-child(2)'
        },
        responsive: true,


        language: {
            sDecimal: ",",
            sEmptyTable: "Tabloda herhangi bir veri mevcut değil",
            sInfo: "_TOTAL_ kayıttan _START_ - _END_ arasındaki kayıtlar gösteriliyor",
            sInfoEmpty: "Kayıt yok",
            sInfoFiltered: "(_MAX_ kayıt içerisinden bulunan)",
            sInfoPostFix: "",
            sInfoThousands: ".",
            sLengthMenu: "Sayfada _MENU_ kayıt göster",
            sLoadingRecords: "Yükleniyor...",
            sProcessing: "İşleniyor...",
            sSearch: "Ara:",
            sZeroRecords: "Eşleşen kayıt bulunamadı",
            oPaginate: {
                sFirst: "İlk",
                sLast: "Son",
                sNext: "Sonraki",
                sPrevious: "Önceki"
            },
            oAria: {
                sSortAscending: ": artan sütun sıralamasını aktifleştir",
                sSortDescending: ": azalan sütun sıralamasını aktifleştir"
            },
            select: {
                rows: {
                    _: "%d kayıt seçildi",
                    "0": "",
                    "1": "1 kayıt seçildi"
                }
            }
        },
        columnDefs: [{
                targets: [0,10],
                visible: false,
                searchable: false
            },
            {
                target: 5, //index of column
                type: "datetime-moment"
            }
        ],

        order: [
            [4, "desc"],
            [9, "desc"]
        ],

        orderCellsTop: true,
        fixedHeader: true
    });

    $.fn.dataTable.moment("DD/MM/YYYY HH:mm");



    total = 0;
    won = 0;
    $.ajax({
        url: "rb3.json",
        type: "GET",
        dataType: "text",
        success: function(data, textStatus, request) {
            try {
                var lastModified = new Date(request.getResponseHeader("Last-Modified")).toLocaleString();

                output = JSON.parse(data);
                $.each(output, function(i, item) {
                    var date = item.Gun + " " + item.Saat;
                    var teams = item.Home + " - " + item.Away;
                    if (item.Live == -1) {

                        var row = table.row
                            .add([
                                i,
                                item.League,
                                item.Hafta,
                                teams,
                                date,
                                item.Bet,
                                item.BetID,
                                "%"+(parseFloat(item.Prob)*100).toFixed(2),
                                item.Odds
                            ])
                            .draw();
                        row.nodes().to$().attr('id', 'mac' + i);

                    } else if (item.Live == -2) {

                        var row = tablebiten.row
                            .add([
                                i,
                                item.League,
                                item.Hafta,
                                teams,
                                date,
                                item.Bet,
                                "%"+(parseFloat(item.Prob)*100).toFixed(2),
                                item.Odds,
                                item.Skor,
                                item.Status
                            ])
                            .draw();
                        row.nodes().to$().attr('id', 'biten' + i);
                        won = won + parseFloat(item.Status);
                        total = total + 1;

                    } else if (item.Live >= 0 || item.Live == "IY") {

                        var row = tablecanli.row
                            .add([
                                i,
                                item.League,
                                item.Hafta,
                                teams,
                                date,
                                item.Bet,
                                item.BetID,
                                "%"+(parseFloat(item.Prob)*100).toFixed(2),
                                item.Odds,
                                item.Skor + "<br><b><span class='blinking'>" + item.Live + "'</span></b>",
                                item.Status
                            ])
                            .draw();
                        row.nodes().to$().attr('id', 'canli' + i);


                    }

                });

                x = ((total - won) / total).toFixed(2);
                $("#failed").html(100 - (x * 100));
                $("#lastupdate").append(lastModified);
                // $( "#tabs" ).tabs( "option", "active" ,0 );
                $('#myTab a[href="#tabs-1"]').tab('show') // Select tab by name

            } catch (e) {
                console.log("error: " + e);
                $("#loading").html('<center>Bir hata oluştu!<br><span style="font-size: 64px;color: #ff0000;" aria-hidden="true">&times;</span></center>');
            }
        },
        error: function(request, error) {
            console.log("AJAX Call Error: " + error);
            $("#loading").html('<center>Bir hata oluştu!<br><span style="font-size: 64px;color: #ff0000;" aria-hidden="true">&times;</span></center>');
        }
    });



    $('#tableRegister tbody').on('click', 'td:not(:first-child)', function () {
        $(this).closest('tr').toggleClass('selected');
        $('#kuponyap').click();

    });







    $("#kuponyap").click(function() {
        if (
            table
            .rows(".selected")
            .data()
            .pluck(0)
            .toArray().length != 0
        ) {
            var macsayisi = table.rows(".selected").data().pluck(0).toArray().length;
            var matcheslist = table.rows(".selected").data().pluck(0).toArray();
            var trHTML = "";
            var analysis = 1;
            oddsp = 1;
            $.each(output, function(i, item) {
                if (jQuery.inArray(i, matcheslist) !== -1) {
                    trHTML = trHTML +
                    '<div class="couponRow outer " id="kupondata' + i + '">' +
                    '<div class="eventName " onclick=""> ' + item.Home +  ' - ' + item.Away +'</div>' +
                    '   <div class="eventCancelBtn">' +
                   '<button type="button" onclick=\"slideonlyone(' + i + ');\" class="close" aria-label="Close"><span aria-hidden="true">&times;</span></button>' +
                     '   </div>' +
                       ' <span class="clearfix"></span>' +
                       ' <div class="eventCode"><b>'+item.BetID +'</b></div>' +
                      '  <div class="eventDate">' + item.Gun + ' - ' + item.Saat +'</div>' +
                   '     <span class="clearfix"></span>' +
                     '   <div class="eventType">' +
                           ' <span class="type">Toplam Gol</span>' +
                     '       <span class="choice" onclick="">'+  item.Bet +'</span>' +
                 '       </div>' +
                    '    <div class="eventOutcome up">' +
                    '        <i class="ni ni-lock"></i>' +
                     '       <span>' +  item.Odds + '</span>' +
                    '    </div>' +
                     '   <div class="status">' +
                    '        <i class="ni">%'+ (parseFloat(item.Prob)*100).toFixed(2)  +'</i>' +
                    '    </div>' +
                    '    <span class="clearfix"></span>'+
                  '  </div>';

                    analysis = analysis * parseFloat(item.Prob).toFixed(4);
                    oddsp = oddsp * item.Odds;
                }
            });

            calculatedata(oddsp, analysis, macsayisi);

            $("#kuponbilgileri").html(trHTML);

              $("#nullcoupon").hide();
              $("#kuponbilgileri").show();
              $("#kuponbilgileritaban").show();


        } else {
       $("#nullcoupon").show();
       $("#kuponbilgileri").hide();
       $("#kuponbilgileritaban").hide();
       $("#macsayisi").html('0');

        }
    });

    $("#kasabilgi").keydown(function() {
        var that = this;
        setTimeout(function() {
            var val = $("#kasabilgi").val();

            if (parseFloat(kellyp).toFixed(2) > 0) {
                $("#kellyproduct").html(parseFloat(val * kellyp).toFixed(2) + " TL"
                );
                $("#winamount").html((val * kellyp * oddsp).toFixed(2) + " TL");
            } else {
                $("#kellyproduct").html(parseFloat(val).toFixed(2) + " TL"
                );
                $("#winamount").html((val * oddsp).toFixed(2) + " TL");
            }

            if (val.length === 0) {
                if (parseFloat(kellyp).toFixed(2) > 0) {
                    $("#kellyproduct").html(parseFloat(kellyp).toFixed(2));
                } else {
                    $("#kellyproduct").html("<b>Oynama</b>");
                }
                $("#oddproduct").html(oddsp.toFixed(2));
            }
        }, 100);
    });




    $('#tableRegister').parent().addClass('table-responsive');



});
