import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

WebUI.navigateToUrl('http://127.0.0.1:8000/login/?next=/tienda_trabajador/')

WebUI.setText(findTestObject('Object Repository/Page_home/input__username'), 'eladmin@gmail.com')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_home/input__password'), 'AUtK+SDyPd0=')

WebUI.click(findTestObject('Object Repository/Page_home/button_Iniciar Sesin'))

WebUI.click(findTestObject('Object Repository/Page_Mi_cuenta_admin/a_Adminstrar Vehiculos'))

WebUI.click(findTestObject('Object Repository/Page_adm producto/a_Modificar producto'))

WebUI.doubleClick(findTestObject('Object Repository/Page_Tienda Online/input__nombre'))

WebUI.setText(findTestObject('Object Repository/Page_Tienda Online/input__nombre'), 'Camioneta vieja')

WebUI.setText(findTestObject('Object Repository/Page_Tienda Online/input__stock'), '1')

WebUI.setText(findTestObject('Object Repository/Page_Tienda Online/input__descripcin'), 'auto en estado indescriptible Detalle: le falta el motor')

WebUI.setText(findTestObject('Object Repository/Page_Tienda Online/input__precio'), '500')

WebUI.click(findTestObject('Object Repository/Page_Tienda Online/input_productosedan_viejo.png_btn btn-warni_db445d'))

WebUI.closeBrowser()

