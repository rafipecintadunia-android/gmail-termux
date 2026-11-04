package id.widodo.ordermandiri;
import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;
public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        WebView wv = new WebView(this);
        wv.setWebViewClient(new WebViewClient());
        wv.getSettings().setJavaScriptEnabled(true);
        // Ganti URL ini dengan server bot kamu kalau ada
        wv.loadUrl("https://github.com/rafipecintadunia-and/AplikasiBebas");
        setContentView(wv);
    }
}
