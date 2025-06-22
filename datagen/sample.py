"""Samples."""

from datetime import date
import random

from pydantic import BaseModel, Field

import utils


class Sample(BaseModel):
    """Represent a single sample."""

    id: str = Field(min_length=1, description="unique ID")
    grid: str = Field(min_length=1, description="grid ID")
    x: int = Field(ge=0, description="X coordinate")
    y: int = Field(ge=0, description="Y coordinate")
    person: str = Field(description="collector")
    when: date = Field(description="when sample was collected")
    mass: float = Field(gt=0.0, description="sample mass")

    @staticmethod
    def make(params, grids, persons):
        """Make a sample."""
        utils.ensure_id_generator(Sample, "S", 4)
        grid = random.choice(grids)
        x = random.randint(0, grid.size - 1)
        y = random.randint(0, grid.size - 1)
        person = random.choice(persons)
        when = utils.random_date(params.sample_date_min, params.sample_date_max)
        mass = round(
            random.uniform(
                params.sample_mass_min,
                params.sample_mass_max,
            ),
            params.precision,
        )
        return Sample(
            id=next(Sample._id_gen),
            grid=grid.id,
            x=x,
            y=y,
            person=person.id,
            when=when,
            mass=mass,
        )

    @staticmethod
    def csv_header():
        """Generate header for CSV file."""
        return "sample_id,grid_id,x,y,person,when,mass"

    def __str__(self):
        """Convert to CSV string."""
        return f"{self.id},{self.grid},{self.x},{self.y},{self.person},{self.when},{self.mass}"
