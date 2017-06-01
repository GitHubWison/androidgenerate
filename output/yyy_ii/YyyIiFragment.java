import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

public class YyyIiFragment extends Fragment {
    private YyyIiViewModel viewModel;
    public static YyyIiFragment newInstance() {

        Bundle args = new Bundle();

        YyyIiFragment fragment = new YyyIiFragment();
        fragment.setArguments(args);
        return fragment;
    }
    @Override
    public View onCreateView(LayoutInflater inflater,  ViewGroup container,  Bundle savedInstanceState) {
        FragmentYyyIiBinding binding = FragmentYyyIiBinding.inflate(inflater,container,false);
        binding.setViewmodel(viewModel);
        return binding.getRoot();
    }

    public void setViewModel(YyyIiViewModel viewModel) {
        this.viewModel = viewModel;
    }
}
