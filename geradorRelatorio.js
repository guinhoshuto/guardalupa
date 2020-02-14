function onOpen(){
  var ui = SpreadsheetApp.getUi();
  ui.createMenu('GetValues')
      .addItem('Gerar Relatório', 'geraRelatorio')
      .addToUi();
}
//Planilha de Monitoramento
var planilhaMonitoramento = SpreadsheetApp.openByUrl("https://docs.google.com/spreadsheets/d/13Y1JRsLksXmHEBKzKiF10HtjpgQn9hDOWGGGqbg6ByE/edit#gid=0").getSheetByName('Sites');

//var abas = planilhaDestino.getSheets();
//var config = planilhaDestino.getSheetByName('config');
//var config = planilhaDestino.getSheetByName('config');

// Create and open a document.
function geraRelatorio(){
    var numRows = planilhaMonitoramento.getLastRow(); 
    var sites = planilhaMonitoramento.getRange('A2:L' + numRows).getValues();
    Logger.log(numRows);
    var sitesGerar = [];
    fr (var len=0;  len<numRows; len++) {

       if(sites[len][0] == 'x'){
            var agencia = sites[len][2];
            var pi = sites[len][3];
            var cliente = sites[len][4];
            var campanha = sites[len][5];
            var siteNome = sites[len][6];
            var inicioData = sites[len][10];
            var fimData = sites[len][11];
                            
            //var inicioData = new Date(inicio.split('/')[2],inicio.split('/')[1],inicio.split('/')[0]);
            
            //var fimData = new Date(fim.split('/')[2],fim.split('/')[1],fim.split('/')[0]);
            const oneDay = 24 * 60 * 60 * 1000;
            var qntDias = Math.round(Math.abs((fimData - inicioData) / oneDay));
            Logger.log(pi + siteNome + ' ' + qntDias + ' ' + inicioData + ' ' + fimData);
            doc = DocumentApp.create(pi + ' - ' + cliente + ' -' + campanha + ' - ' + siteNome);
            var body = doc.getBody();
            var wsi = UrlFetchApp.fetch('http://vendo-bolo.com/monitoramento/wsi.jpg');

            doc.getChild(0).asParagraph().appendInlineImage(wsi.getBlob());

            var days = [['01','02'],['x','x']]; 
            doc.getBody().appendTable(days);

       } 
    }

}
o
