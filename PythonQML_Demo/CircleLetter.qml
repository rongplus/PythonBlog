import QtQuick 2.6
import QtQuick.Controls 2.0
import QtQuick.Controls.Material 2.0
import QtQuick.Layouts 1.12

Rectangle {
    id:accountCapital
    color: "blue"                                    
    width:40
    height:40
    radius: 20
    property string text: ""
    
    Text {
        id: usaerProfileLetter                          
        anchors.centerIn: parent
        text: 'a'
        color:"white"
        font.pointSize: 20
        font.capitalization:Font.Capitalize
    }
    
    Rectangle {
        id: mask
        width:150
        height:150
        radius: 75
        visible: false
    }
}