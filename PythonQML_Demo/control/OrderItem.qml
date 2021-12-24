
import QtQuick 2.6
import QtQuick.Controls 2.0
import QtQuick.Controls.Material 2.0
import QtQuick.Layouts 1.12

Rectangle{
    width: parent.width*0.95
    property  alias  data111: mainRect.data111
    anchors.             rightMargin:10
    height: 90
    Rectangle{
        id:mainRect
        x:10

        width: parent.width
        height: 80
        anchors.leftMargin:10
        anchors.rightMargin:10
        // Layout.alignment: Qt.AlignCenter
        color: ListView.isCurrentItem ? "#003366" : "#585858"
        border.color: "blue"
        //color: "transparent"
        border.width: 1
        property var data111: []

        property string material: "3d Meaterial"
        property string reinforced: "3d reinforced"
        property string printer: "3d printer"
        property string needTime: "3d time"



        RowLayout
        {
           height:parent.height
           width:parent.width
            anchors.leftMargin:10
            anchors.rightMargin:10
            Rectangle {
                Layout.alignment: Qt.AlignCenter
                
                //color: "transparent"
                width:50
                height:50
                //color: 'gray'
                Image {
                id:itemImg
                    anchors.fill: parent
                    anchors.topMargin:20
                     
                    Layout.alignment: Qt.AlignCenter
                    fillMode: Image.PreserveAspectFit
                    source: "Active.png"
                }
            
            }

            Rectangle {
                width:parent.width*0.6
                height:80
                anchors.leftMargin:10
                y:0
                color: ListView.isCurrentItem ? "red" : "#585858"
                Text{  
                    id:nameLabel
                    anchors.leftMargin:10
                    x:10
                    y:5             
                    //color: "white"
                     color: ListView.isCurrentItem ? "red" : "blue"
                    text: mainRect.data111['name']
                }

                Text{  
                    x:10
                    id:firstLine
                    anchors.top :nameLabel.bottom    
                    anchors.topMargin:10  
                    anchors.leftMargin:10
                    //color: "white"
                    text: "<b>  Material:  </b>" +mainRect.material + "<b> Reinforced Material: </b>" + mainRect.reinforced 
                }

                Text{  
                    x:10
                    id:nextLine
                    anchors.top :firstLine.bottom    
                    anchors.topMargin:10  
                    anchors.leftMargin:10
                    //color: "white"
                    text: "<b>  Printer:  </b>" +mainRect.printer + "<b> Time of Print: </b>" + mainRect.needTime 
                }        
            }

            Rectangle {
            width:60
            height:40
                Button{          
                anchors.fill: parent
                    text: "PRINT"
                }
            }
        
            MyIconButton{img_src:"bin.png"}

        }

        

        MouseArea {
            anchors.fill: parent
            onClicked: 
            {console.log("log, click item")
        listView.currentIndex = index }
        }
    }
}

