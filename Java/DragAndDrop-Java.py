import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.interactions.Action;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.interactions.Keyboard;
import org.openqa.selenium.interactions.Mouse;
import org.openqa.selenium.remote.server.Session;
import org.openqa.selenium.remote.server.handler.interactions.MouseMoveToLocation;

import java.awt.event.MouseMotionListener;
import org.openqa.selenium.support.ui.WebDriverWait;

public class DragAndDrop {
    public static void main(String[] args) throws InterruptedException {

        System.setProperty("webdriver.chrome.driver", "F:/Downloads/chromedriver.exe");
//        System.setProperty("webdriver.gecko.driver", "F:/Downloads/geckodriver.exe");

        WebDriver driver = new ChromeDriver();
//        WebDriver driver = new FirefoxDriver();

        driver.get("https://formy-project.herokuapp.com/dragdrop");

            WebElement image = driver.findElement(By.id("image"));

            WebElement box = driver.findElement(By.id("box"));

//            Actions actions = new Actions(driver);
//            actions.dragAndDrop(image, box).build().perform();

        final String java_script =
                "var src=arguments[0],tgt=arguments[1];var dataTransfer={dropEffe" +
                        "ct:'',effectAllowed:'all',files:[],items:{},types:[],setData:fun" +
                        "ction(format,data){this.items[format]=data;this.types.append(for" +
                        "mat);},getData:function(format){return this.items[format];},clea" +
                        "rData:function(format){}};var emit=function(event,target){var ev" +
                        "t=document.createEvent('Event');evt.initEvent(event,true,false);" +
                        "evt.dataTransfer=dataTransfer;target.dispatchEvent(evt);};emit('" +
                        "dragstart',src);emit('dragenter',tgt);emit('dragover',tgt);emit(" +
                        "'drop',tgt);emit('dragend',src);";
        JavascriptExecutor js = (JavascriptExecutor)driver;
        Thread.sleep(2000);

        js.executeScript(java_script, image, box);
        Thread.sleep(2000);

        driver.quit();
    }
}
