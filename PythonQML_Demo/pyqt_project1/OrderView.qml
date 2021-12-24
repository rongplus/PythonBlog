import QtQuick 2.6
import QtQuick.Controls 2.0
import QtQuick.Controls.Material 2.0
import QtQuick.Layouts 1.12


 Rectangle {
     width: 700; height: 200
     color:"white"

     property variant lt: [ {name: "Bill Smith",
            position: "Engineer"},{
            name: "John Brown",
            position: "Engineer"
        },{
            name: "Sam Wise",
            position: "Manager"
        },{name: "Bill Smith",
            position: "Engineer"},{
            name: "John Brown",
            position: "Engineer"
        },{
            name: "Sam Wise",
            position: "Manager"
        }]

      Rectangle
      {
          id: menuRect
          y:5
          height:30
          anchors.leftMargin:10
          Text {
              x:10
              text: "Refresh Orders"
          
          }

          Text {
              x: 200
              text: "Orders"
          
          }
      }
    
     ListView 
     {
            id: listView
             anchors.top:menuRect.bottom
             anchors.bottom:parent.bottom
             anchors.left:parent.left
             anchors.right:parent.right

            flickableDirection: Flickable.VerticalFlick
            boundsBehavior: Flickable.StopAtBounds
            model: lt
            clip: true
            delegate:   OrderItem 
            {
                data111 :model.modelData
                onBack: {
                    listView.currentIndex = index 
                    console.log("log, click item", index)
                }
            }

            Layout.fillWidth: true
            Layout.fillHeight: true
            highlight: Rectangle { color: "lightsteelblue"; radius: 5 }

            ScrollBar.vertical: ScrollBar {}
           
        }
 }