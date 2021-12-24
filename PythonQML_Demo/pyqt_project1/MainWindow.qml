import QtQuick 2.15
import QtQuick.Controls 2.15

import QtQuick.Dialogs 1.2
import QtQuick.Window 2.2
import QtQuick 2.3
 
 
 
Rectangle  {
    
    visible:true
    //anchors.fill:parent
    height:400
    width:400
    color:"yellow"

    function displayNumber() {
        console.log("from python");
        messageDialog.close()
        
    }


    Button
    {
        x:10
        y:10
        text:"Show Order"
        onClicked:{
            mainView.onStart(0)
            messageDialog.open()
            }
    }

    MessageDialog {
        id: messageDialog
        title: "Failed to update profile image!"
        text: "Failed to update profile image!"
        onAccepted: {
            console.log("And of course you could only agree.")
            //hide()
        }
        //Component.onCompleted: visible = true
    }



 
 
 
}